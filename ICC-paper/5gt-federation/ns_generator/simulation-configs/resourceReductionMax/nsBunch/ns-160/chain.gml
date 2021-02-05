graph [
  node [
    id 0
    label 1
    disk 7
    cpu 4
    memory 1
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 3
    memory 12
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 3
    memory 2
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 4
    memory 13
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 4
    memory 13
  ]
  node [
    id 5
    label 6
    disk 5
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
    delay 32
    bw 96
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 188
  ]
  edge [
    source 0
    target 2
    delay 35
    bw 147
  ]
  edge [
    source 0
    target 3
    delay 25
    bw 143
  ]
  edge [
    source 1
    target 4
    delay 30
    bw 185
  ]
  edge [
    source 2
    target 4
    delay 26
    bw 193
  ]
  edge [
    source 3
    target 5
    delay 35
    bw 52
  ]
  edge [
    source 4
    target 5
    delay 26
    bw 111
  ]
]
