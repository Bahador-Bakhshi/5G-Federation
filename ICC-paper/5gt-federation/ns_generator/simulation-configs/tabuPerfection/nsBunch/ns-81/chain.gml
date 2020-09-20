graph [
  node [
    id 0
    label 1
    disk 9
    cpu 4
    memory 7
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 4
    memory 11
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 3
    memory 11
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 4
    memory 5
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 3
    memory 13
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 3
    memory 10
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 62
  ]
  edge [
    source 0
    target 1
    delay 30
    bw 134
  ]
  edge [
    source 0
    target 2
    delay 29
    bw 184
  ]
  edge [
    source 0
    target 3
    delay 35
    bw 191
  ]
  edge [
    source 1
    target 4
    delay 26
    bw 193
  ]
  edge [
    source 2
    target 4
    delay 31
    bw 115
  ]
  edge [
    source 3
    target 4
    delay 30
    bw 94
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 96
  ]
]
