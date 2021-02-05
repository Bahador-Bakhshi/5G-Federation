graph [
  node [
    id 0
    label 1
    disk 6
    cpu 4
    memory 5
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 3
    memory 2
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 3
    memory 1
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 4
    memory 8
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 3
    memory 9
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 3
    memory 9
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 181
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 56
  ]
  edge [
    source 0
    target 2
    delay 34
    bw 184
  ]
  edge [
    source 1
    target 3
    delay 26
    bw 61
  ]
  edge [
    source 2
    target 3
    delay 34
    bw 70
  ]
  edge [
    source 3
    target 4
    delay 31
    bw 122
  ]
  edge [
    source 4
    target 5
    delay 35
    bw 103
  ]
]
