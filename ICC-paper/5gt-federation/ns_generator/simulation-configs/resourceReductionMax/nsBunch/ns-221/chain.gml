graph [
  node [
    id 0
    label 1
    disk 6
    cpu 1
    memory 3
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 3
    memory 13
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 4
    memory 6
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 2
    memory 1
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 4
    memory 3
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 1
    memory 7
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 141
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 111
  ]
  edge [
    source 0
    target 2
    delay 31
    bw 80
  ]
  edge [
    source 0
    target 3
    delay 27
    bw 178
  ]
  edge [
    source 1
    target 4
    delay 27
    bw 124
  ]
  edge [
    source 2
    target 5
    delay 25
    bw 82
  ]
  edge [
    source 3
    target 5
    delay 29
    bw 70
  ]
  edge [
    source 4
    target 5
    delay 26
    bw 60
  ]
]
