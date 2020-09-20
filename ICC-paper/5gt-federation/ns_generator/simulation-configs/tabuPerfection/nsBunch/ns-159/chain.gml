graph [
  node [
    id 0
    label 1
    disk 1
    cpu 2
    memory 13
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 1
    memory 4
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 4
    memory 12
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 2
    memory 9
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 1
    memory 4
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 2
    memory 10
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 169
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 148
  ]
  edge [
    source 1
    target 2
    delay 26
    bw 109
  ]
  edge [
    source 1
    target 3
    delay 25
    bw 120
  ]
  edge [
    source 1
    target 4
    delay 27
    bw 117
  ]
  edge [
    source 2
    target 5
    delay 32
    bw 138
  ]
  edge [
    source 3
    target 5
    delay 29
    bw 95
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 100
  ]
]
