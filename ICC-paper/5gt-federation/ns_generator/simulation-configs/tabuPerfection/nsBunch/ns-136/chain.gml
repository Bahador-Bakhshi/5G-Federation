graph [
  node [
    id 0
    label 1
    disk 3
    cpu 4
    memory 13
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 4
    memory 16
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 2
    memory 14
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 3
    memory 14
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 3
    memory 14
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 1
    memory 10
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 117
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 71
  ]
  edge [
    source 0
    target 2
    delay 30
    bw 169
  ]
  edge [
    source 0
    target 3
    delay 35
    bw 94
  ]
  edge [
    source 1
    target 4
    delay 28
    bw 85
  ]
  edge [
    source 2
    target 4
    delay 35
    bw 55
  ]
  edge [
    source 3
    target 4
    delay 28
    bw 198
  ]
  edge [
    source 4
    target 5
    delay 30
    bw 190
  ]
]
