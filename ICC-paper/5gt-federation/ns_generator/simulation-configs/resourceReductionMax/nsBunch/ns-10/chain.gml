graph [
  node [
    id 0
    label 1
    disk 10
    cpu 1
    memory 11
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 1
    memory 7
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 2
    memory 5
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 1
    memory 12
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 3
    memory 2
  ]
  node [
    id 5
    label 6
    disk 6
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
    delay 34
    bw 114
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 62
  ]
  edge [
    source 0
    target 2
    delay 33
    bw 83
  ]
  edge [
    source 1
    target 3
    delay 34
    bw 136
  ]
  edge [
    source 2
    target 3
    delay 33
    bw 149
  ]
  edge [
    source 3
    target 4
    delay 29
    bw 194
  ]
  edge [
    source 4
    target 5
    delay 29
    bw 140
  ]
]
