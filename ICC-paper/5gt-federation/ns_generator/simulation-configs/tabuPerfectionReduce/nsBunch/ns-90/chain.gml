graph [
  node [
    id 0
    label 1
    disk 7
    cpu 1
    memory 3
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 1
    memory 2
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 4
    memory 13
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 3
    memory 6
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 4
    memory 12
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 3
    memory 2
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 28
    bw 85
  ]
  edge [
    source 0
    target 1
    delay 25
    bw 136
  ]
  edge [
    source 0
    target 2
    delay 32
    bw 161
  ]
  edge [
    source 1
    target 4
    delay 26
    bw 170
  ]
  edge [
    source 2
    target 3
    delay 35
    bw 134
  ]
  edge [
    source 3
    target 5
    delay 25
    bw 159
  ]
  edge [
    source 4
    target 5
    delay 32
    bw 123
  ]
]
