graph [
  node [
    id 0
    label 1
    disk 7
    cpu 2
    memory 8
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 4
    memory 12
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 3
    memory 5
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 4
    memory 4
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 1
    memory 6
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 1
    memory 4
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 26
    bw 140
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 139
  ]
  edge [
    source 1
    target 2
    delay 32
    bw 92
  ]
  edge [
    source 1
    target 3
    delay 34
    bw 120
  ]
  edge [
    source 1
    target 4
    delay 25
    bw 82
  ]
  edge [
    source 2
    target 5
    delay 33
    bw 139
  ]
  edge [
    source 3
    target 5
    delay 29
    bw 56
  ]
  edge [
    source 4
    target 5
    delay 34
    bw 153
  ]
]
