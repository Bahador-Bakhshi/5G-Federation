graph [
  node [
    id 0
    label 1
    disk 7
    cpu 2
    memory 4
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 2
    memory 16
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 3
    memory 4
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 1
    memory 11
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 3
    memory 10
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 2
    memory 5
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 133
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 161
  ]
  edge [
    source 0
    target 2
    delay 27
    bw 93
  ]
  edge [
    source 1
    target 4
    delay 31
    bw 124
  ]
  edge [
    source 2
    target 3
    delay 34
    bw 163
  ]
  edge [
    source 3
    target 4
    delay 26
    bw 67
  ]
  edge [
    source 4
    target 5
    delay 31
    bw 193
  ]
]
