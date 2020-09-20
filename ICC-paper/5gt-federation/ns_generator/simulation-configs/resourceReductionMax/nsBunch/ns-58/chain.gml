graph [
  node [
    id 0
    label 1
    disk 5
    cpu 4
    memory 11
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 4
    memory 14
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 3
    memory 5
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 4
    memory 8
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 3
    memory 10
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 3
    memory 4
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 35
    bw 106
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 172
  ]
  edge [
    source 1
    target 2
    delay 27
    bw 128
  ]
  edge [
    source 2
    target 3
    delay 27
    bw 55
  ]
  edge [
    source 2
    target 4
    delay 27
    bw 53
  ]
  edge [
    source 2
    target 5
    delay 26
    bw 152
  ]
]
